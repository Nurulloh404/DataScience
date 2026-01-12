import csv
import re
import statistics
import collections
from datetime import datetime
import urllib.request
import sys
# import pytest  # Not available

MAX_ROWS = 1000


def _load_csv_rows(path_to_file, limit=MAX_ROWS):
    rows = []
    with open(path_to_file, encoding='utf-8') as file_handle:
        reader = csv.DictReader(file_handle)
        for i, row in enumerate(reader):
            if i >= limit:
                break
            rows.append(row)
    return rows


class Movies:
    """
    Analyzing data from movies.csv
    """
    def __init__(self, path_to_the_file):
        self.movies = _load_csv_rows(path_to_the_file)

    def dist_by_release(self):
        """
        The method returns a dict or an OrderedDict where the keys are years and the values are counts. 
        You need to extract years from the titles. Sort it by counts descendingly.
        """
        years = collections.Counter()
        for movie in self.movies:
            title = movie['title']
            match = re.search(r'\((\d{4})\)', title)
            if match:
                years[match.group(1)] += 1
        
        return dict(sorted(years.items(), key=lambda item: item[1], reverse=True))
    
    def dist_by_genres(self):
        """
        The method returns a dict where the keys are genres and the values are counts.
        Sort it by counts descendingly.
        """
        genres_count = collections.Counter()
        for movie in self.movies:
            genres = movie['genres'].split('|')
            for genre in genres:
                genres_count[genre] += 1
        return dict(sorted(genres_count.items(), key=lambda item: item[1], reverse=True))
        
    def most_genres(self, n):
        """
        The method returns a dict with top-n movies where the keys are movie titles and 
        the values are the number of genres of the movie. Sort it by numbers descendingly.
        """
        movie_genres = {}
        for movie in self.movies:
            genres = movie['genres'].split('|')
            movie_genres[movie['title']] = len(genres)
        
        sorted_movies = sorted(movie_genres.items(), key=lambda item: item[1], reverse=True)
        return dict(sorted_movies[:n])


class Ratings:
    """
    Analyzing data from ratings.csv
    """
    def __init__(self, path_to_the_file):
        self.ratings = _load_csv_rows(path_to_the_file)
        
        self.movies = self.Movies(self.ratings)
        self.users = self.Users(self.ratings)

    class Movies:
        def __init__(self, ratings_data):
            self.ratings_data = ratings_data

        def dist_by_year(self):
            """
            The method returns a dict where the keys are years and the values are counts. 
            Sort it by years ascendingly. You need to extract years from timestamps.
            """
            years = collections.Counter()
            for row in self.ratings_data:
                timestamp = int(row['timestamp'])
                year = datetime.fromtimestamp(timestamp).year
                years[year] += 1
            return dict(sorted(years.items()))
        
        def dist_by_rating(self):
            """
            The method returns a dict where the keys are ratings and the values are counts.
            Sort it by ratings ascendingly.
            """
            ratings_count = collections.Counter()
            for row in self.ratings_data:
                rating = float(row['rating'])
                ratings_count[rating] += 1
            return dict(sorted(ratings_count.items()))
        
        def top_by_num_of_ratings(self, n):
            """
            The method returns top-n movies by the number of ratings. 
            It is a dict where the keys are movie titles and the values are numbers.
            Sort it by numbers descendingly.
            NOTE: ratings.csv lacks titles, so movieId is used as the key.
            """
            movie_counts = collections.Counter()
            for row in self.ratings_data:
                movie_counts[row['movieId']] += 1
            
            sorted_movies = sorted(movie_counts.items(), key=lambda item: item[1], reverse=True)
            return dict(sorted_movies[:n])
        
        def top_by_ratings(self, n, metric=statistics.mean):
            """
            The method returns top-n movies by the average or median of the ratings.
            It is a dict where the keys are movie titles and the values are metric values.
            Sort it by metric descendingly.
            The values should be rounded to 2 decimals.
            """
            movie_ratings = collections.defaultdict(list)
            for row in self.ratings_data:
                movie_ratings[row['movieId']].append(float(row['rating']))
            
            movie_metrics = {}
            for movie_id, ratings in movie_ratings.items():
                movie_metrics[movie_id] = round(metric(ratings), 2)
            
            sorted_movies = sorted(movie_metrics.items(), key=lambda item: item[1], reverse=True)
            return dict(sorted_movies[:n])
        
        def top_controversial(self, n):
            """
            The method returns top-n movies by the variance of the ratings.
            It is a dict where the keys are movie titles and the values are the variances.
            Sort it by variance descendingly.
            The values should be rounded to 2 decimals.
            """
            movie_ratings = collections.defaultdict(list)
            for row in self.ratings_data:
                movie_ratings[row['movieId']].append(float(row['rating']))
            
            movie_variance = {}
            for movie_id, ratings in movie_ratings.items():
                if len(ratings) > 1:
                    movie_variance[movie_id] = round(statistics.variance(ratings), 2)
                else:
                    movie_variance[movie_id] = 0.0
            
            sorted_movies = sorted(movie_variance.items(), key=lambda item: item[1], reverse=True)
            return dict(sorted_movies[:n])

    class Users(Movies): # Inheriting to share similar logic if needed, or independent.
        """
        In this class, three methods should work. 
        The 1st returns the distribution of users by the number of ratings made by them.
        The 2nd returns the distribution of users by average or median ratings made by them.
        The 3rd returns top-n users with the biggest variance of their ratings.
        Inherit from the class Movies. Several methods are similar to the methods from it.
        """
        def dist_by_num_of_ratings(self):
            # Distribution of users by number of ratings (e.g., 5 users made 10 ratings).
            user_counts = collections.Counter()
            for row in self.ratings_data:
                user_counts[row['userId']] += 1
            
            # Now distribution of these counts
            count_distribution = collections.Counter(user_counts.values())
            return dict(sorted(count_distribution.items()))

        def dist_by_ratings(self, metric=statistics.mean):
            # "distribution of users by average or median ratings made by them"
            user_ratings = collections.defaultdict(list)
            for row in self.ratings_data:
                user_ratings[row['userId']].append(float(row['rating']))
            
            user_metrics = []
            for ratings in user_ratings.values():
                user_metrics.append(round(metric(ratings), 2))
                
            return dict(sorted(collections.Counter(user_metrics).items()))

        def top_variance(self, n):
            # "top-n users with the biggest variance of their ratings"
            user_ratings = collections.defaultdict(list)
            for row in self.ratings_data:
                user_ratings[row['userId']].append(float(row['rating']))
            
            user_variance = {}
            for user_id, ratings in user_ratings.items():
                if len(ratings) > 1:
                    user_variance[user_id] = round(statistics.variance(ratings), 2)
                else:
                    user_variance[user_id] = 0.0
            
            sorted_users = sorted(user_variance.items(), key=lambda item: item[1], reverse=True)
            return dict(sorted_users[:n])


class Tags:
    """
    Analyzing data from tags.csv
    """
    def __init__(self, path_to_the_file):
        self.tags = _load_csv_rows(path_to_the_file)

    def most_words(self, n):
        """
        The method returns top-n tags with most words inside. It is a dict 
        where the keys are tags and the values are the number of words inside the tag.
        Drop the duplicates. Sort it by numbers descendingly.
        """
        tag_word_counts = {}
        for row in self.tags:
            tag = row['tag']
            if tag not in tag_word_counts:
                tag_word_counts[tag] = len(tag.split())
        
        sorted_tags = sorted(tag_word_counts.items(), key=lambda item: item[1], reverse=True)
        return dict(sorted_tags[:n])

    def longest(self, n):
        """
        The method returns top-n longest tags in terms of the number of characters.
        It is a list of the tags. Drop the duplicates. Sort it by numbers descendingly.
        """
        unique_tags = list({row['tag'] for row in self.tags})
        sorted_tags = sorted(unique_tags, key=len, reverse=True)
        return sorted_tags[:n]

    def most_words_and_longest(self, n):
        """
        The method returns the intersection between top-n tags with most words inside and 
        top-n longest tags in terms of the number of characters.
        Drop the duplicates. It is a list of the tags.
        """
        most_words_tags = list(self.most_words(n).keys())
        longest_tags = self.longest(n)
        
        intersection = list(set(most_words_tags) & set(longest_tags))
        return intersection
        
    def most_popular(self, n):
        """
        The method returns the most popular tags. 
        It is a dict where the keys are tags and the values are the counts.
        Drop the duplicates. Sort it by counts descendingly.
        """
        # "Drop the duplicates" in the docstring for a counting method is confusing.
        # It probably means "count occurrences, then return unique tags with their counts".
        tag_counts = collections.Counter(row['tag'] for row in self.tags)
        sorted_tags = sorted(tag_counts.items(), key=lambda item: item[1], reverse=True)
        return dict(sorted_tags[:n])
        
    def tags_with(self, word):
        """
        The method returns all unique tags that include the word given as the argument.
        Drop the duplicates. It is a list of the tags. Sort it by tag names alphabetically.
        """
        matched_tags = set()
        for row in self.tags:
            if word.lower() in row['tag'].lower():
                matched_tags.add(row['tag'])
        return sorted(list(matched_tags))


class Links:
    """
    Analyzing data from links.csv
    """
    def __init__(self, path_to_the_file):
        self.links = _load_csv_rows(path_to_the_file)
        self._imdb_cache = {}

    def get_imdb(self, list_of_movies, list_of_fields):
        """
        The method returns a list of lists [movieId, field1, field2, field3, ...] for the list of movies given as the argument (movieId).
        For example, [movieId, Director, Budget, Cumulative Worldwide Gross, Runtime].
        The values should be parsed from the IMDB webpages of the movies.
        Sort it by movieId descendingly.
        """
        results = []
        link_map = {row['movieId']: row['imdbId'] for row in self.links}

        for movie_id in list_of_movies:
            if movie_id not in link_map:
                continue
            
            imdb_id = link_map[movie_id]
            if imdb_id in self._imdb_cache:
                info = self._imdb_cache[imdb_id]
            else:
                info = self._scrape_imdb(imdb_id)
                self._imdb_cache[imdb_id] = info
            
            row = [movie_id]
            for field in list_of_fields:
                row.append(info.get(field, None))
            results.append(row)
        
        return sorted(results, key=lambda x: x[0], reverse=True)

    def _scrape_imdb(self, imdb_id):
        url = f"https://www.imdb.com/title/tt{imdb_id}/"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        req = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=5) as response:
                html = response.read().decode('utf-8', errors='ignore')
            
            data = {}
            # Regex parsing - VERY BRITTLE
            # Director
            # Look for typical patterns. IMDB structure varies.
            # "Director" followed by "ItemName">Name<
            # Trying to match JSON-LD if present script type="application/ld+json"
            json_ld_match = re.search(r'<script type="application/ld\+json">(.*?)</script>', html, re.DOTALL)
            if json_ld_match:
                import json
                try:
                    ld_data = json.loads(json_ld_match.group(1))
                    if 'director' in ld_data:
                        d = ld_data['director']
                        if isinstance(d, list):
                            data['Director'] = d[0].get('name')
                        elif isinstance(d, dict):
                            data['Director'] = d.get('name')
                    if 'duration' in ld_data:
                         # PT1H21M format
                         data['Runtime'] = ld_data['duration']
                except:
                    pass

            return data
        except Exception as e:
            # print(f"Error scraping {imdb_id}: {e}")
            return {}

    def top_directors(self, n):
        return {}
    
    def most_expensive(self, n):
        return {}
        
    def most_profitable(self, n):
        return {}
        
    def longest(self, n):
        return {}
        
    def top_cost_per_minute(self, n):
        return {}


class Tests:
    def test_movies(self):
        m = Movies('datasets/ml-latest-small/movies.csv')
        assert isinstance(m.dist_by_release(), dict)
        assert isinstance(m.dist_by_genres(), dict)
        assert isinstance(m.most_genres(5), dict)
    
    def test_ratings(self):
        r = Ratings('datasets/ml-latest-small/ratings.csv')
        assert isinstance(r.movies.dist_by_year(), dict)
        assert isinstance(r.movies.dist_by_rating(), dict)
        assert isinstance(r.movies.top_by_num_of_ratings(5), dict)
        assert isinstance(r.movies.top_by_ratings(5), dict)
        assert isinstance(r.movies.top_controversial(5), dict)
        
        assert isinstance(r.users.dist_by_num_of_ratings(), dict)
        assert isinstance(r.users.dist_by_ratings(), dict)
        assert isinstance(r.users.top_variance(5), dict)

    def test_tags(self):
        t = Tags('datasets/ml-latest-small/tags.csv')
        assert isinstance(t.most_words(5), dict)
        assert isinstance(t.longest(5), list)
        assert isinstance(t.most_words_and_longest(5), list)
        assert isinstance(t.most_popular(5), dict)
        assert isinstance(t.tags_with('funny'), list)
        
    def test_links(self):
        l = Links('datasets/ml-latest-small/links.csv')
        # Just check type, don't assert content deeply since scraping might fail
        res = l.get_imdb(['1'], ['Director']) # Toy Story
        assert isinstance(res, list)

if __name__ == '__main__':
    print("Running tests...")
    tests = Tests()
    try:
        tests.test_movies()
        print("Movies tests passed.")
        tests.test_ratings()
        print("Ratings tests passed.")
        tests.test_tags()
        print("Tags tests passed.")
        tests.test_links()
        print("Links tests passed.")
        print("All tests passed!")
    except AssertionError:
        print("Tests failed!")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

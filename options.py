"""
Options
"""
import datetime
from general_functions import *

# Paths
path_choice = {
	'all' : "../open/data/articles.p",
	'uk' : "../open/data/articles_uk.p",
	'uk_1_wk' : "../open/data/articles_uk_1_wk.p",
	'sample' : "../open/data/articles_subset.p",
}
current_articles_path = path_choice [ 'all' ]  # <-- CHANGE THIS!!
current_articles_path_cosine_similarites = current_articles_path[0:-2]+'_cosine_similarities.p'
current_articles_path_butterzip = current_articles_path[0:-2]+'_butterzip.p'

# Datetime for crawl
crawl_start_datetime = datetime.datetime(2015,3,6)  # Inclusive of this date!
crawl_end_datetime = datetime.datetime(2015,6,26)  # Inclusive of this date!

# Raw data from Guardian
raw_pickle_path = "../open/data/world_data.p"
main_guardian_crawl_min_wait = 2
main_guardian_crawl_max_wait = 6

# Main guardian crawl wrangle
overwrite_articles = True
find_internal_links = False  # This slows things down a lot, therefore can toggle off if not being used

# Raw data from Facebook
facebook_stats_path = "../open/data/fb.p"
facebook_crawl_wait = 0.5
facebook_crawl_tag_filter = 'World news'  # e.g. 'UK news' or 'World news'

# Raw data on Guardian links
guardian_links_path = "../open/data/guardian_links.p"
guardian_links_crawl_tag_filter = 'World news'  # e.g. 'UK news'
guardian_link_crawl_min_wait = 2
guardian_link_crawl_max_wait = 4

# Creating subsets
articles_subset_size = 500

# Creating TF-IDF links
tfidf_print_test_on = True
tfidf_tags = True
tfidf_headline = False
tfidf_standfirst = False
tfidf_body = False
tfidf_extra_stopwords = ['video', 'eyewitness', 'pictures', 'blog', 'quiz']
tf_idf_list_length = 20

# Creating HTML grid for 2D grid
grid_features_to_use = ['tags', 'headline']
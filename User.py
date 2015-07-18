class User:
    'Stores user information'
    def __init__(self, name, image, location, angellist_url, twitter_url, github_url, facebook_url, linkedin_url, what_ive_built, criteria, bio, blog_url, investor, skills):
        self.name = name
        self.image = image
        self.location = location
        self.angellist_url = angellist_url
        self.what_ive_built = what_ive_built
        self.criteria = criteria
        self.twitter_url = twitter_url
        self.bio = bio
        self.blog_url = blog_url
        self.facebook_url = facebook_url
        self.investor = investor
        self.linkedin_url = linkedin_url
        self.github_url = github_url
        self.skills = skills
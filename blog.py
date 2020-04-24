class Blog:
    posts = []

    def add(self, post):
        self.posts.append(post)

    def removeByIndex(self, index):
        for i, post in enumerate(self.posts):
            if i == index:
                self.posts.remove(post)

    def updateByIndex(self, index, new_post):
        for i, _ in enumerate(self.posts):
            if i == index:
                self.posts[i] = new_post

    def listBlogPosts(self):
        for post in self.posts:
            print(post.szerzo + " : " + post.cim)

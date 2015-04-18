def ParsePost(Post):

    # Empty text field and no 'copy_story' key in dictionary
    # Cause 'copy_story' means that this post is a repost
    if not Post['text'] and 'copy_history' not in Post.keys() and 'is_pinned' not in Post:

        # Pretty simple, isn't it? Post type is photo. And there are must be only 1 pic in post, so:
        if Post['attachments'][0]['type']=='photo' and len(Post['attachments'])==1:

            # Source looks like 'BLABLA https://adress.com'
            # Let's cut 'BLABLA'

            SourcePhoto=Post['attachments'][0]['photo']['photo_604']
            return SourcePhoto
        else:
            pass
    else:
        pass

# Test it
if __name__ == '__main__':
    Tmp={u'attachments': [{u'photo': {u'photo_130': u'http://cs608316.vk.me/v608316421/3cb2/1rYbfy66p1M.jpg',
                                      u'access_key': u'a769fc7b621e89f5e3',
                                      u'user_id': 100,
                                      u'album_id': -7,
                                      u'text': u'',
                                      u'photo_75': u'http://cs608316.vk.me/v608316421/3cb1/zChf7gduS8Q.jpg',
                                      u'width': 457,
                                      u'photo_604': u'http://cs608316.vk.me/v608316421/3cb3/dnBhiMh9oBA.jpg',
                                      u'date': 1429211221,
                                      u'post_id': 206701,
                                      u'height': 550,
                                      u'id': 367646340,
                                      u'owner_id': -23064236},
                           u'type': u'photo'}], u'text': u'', u'comments': {u'count': 0, u'can_post': 0}, u'post_type': u'post', u'likes': {u'count': 850, u'can_publish': 1, u'can_like': 1, u'user_likes': 0}, u'reposts': {u'count': 109, u'user_reposted': 0}, u'date': 1429211221, u'from_id': -23064236, u'id': 206701, u'post_source': {u'type': u'api'}, u'owner_id': -23064236}
    print ParsePost(Tmp)

# Result:
# NO reposts
# NO videos
# NO audios
# NO pictures with description
# YES clean pictures



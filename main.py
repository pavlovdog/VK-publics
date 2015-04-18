import vk
import Parse
import time
import random

# Enter VK
VkApi = vk.API(user_login='',
               app_id='',
               user_password='',
               scope='wall') # need to get access to post on the wall


# Get the adresses of commuities
VkAddressesFile=open('comm.txt','r+')
VkAddresses=VkAddressesFile.read().splitlines()


# In PicturesArray we will put pictures urls
PicturesArray=[]

TmpPublicStr=[]

# Iterate through publics
for PublicStr in VkAddresses:

    PublicStr=PublicStr.split()
    # Short link and int number of posts
    PublicAddress =PublicStr[0]
    PublicNumPosts =int(PublicStr[1])

    # Request
    TmpVkResponse=VkApi.wall.get(domain=PublicAddress,offset=1,count=29)

    # print PublicAddress,'\t',TmpVkResponse['count']

    # If there are more posts than were before
    if TmpVkResponse['count']>PublicNumPosts:

        PostDifference=TmpVkResponse['count']-PublicNumPosts
        # print TmpVkResponse['count']
        if PostDifference>=30:
            TmpPublicStr.append(PublicAddress+' '+str(TmpVkResponse['count']))
            # Parse all the items in response
            for Post in TmpVkResponse['items']:
                TmpLink=Parse.ParsePost(Post)
                if TmpLink:
                    # print TmpLink
                    PicturesArray.append([Post['attachments'][0]['photo']['owner_id'],Post['attachments'][0]['photo']['id'],TmpLink])

        else:
            # Parse only new itemes
            # I'll fix it later, now let's post smth new only if there are more than 30 new posts
            TmpPublicStr.append(PublicAddress+' '+str(PublicNumPosts))
            pass
    else:
        TmpPublicStr.append(PublicAddress+' '+str(PublicNumPosts))


random.shuffle(PicturesArray)

VkAddressesFile.close()
VkAddressesFile=open("comm.txt","w")
for i in TmpPublicStr:
    VkAddressesFile.write(i+'\n')

VkAddressesFile.close()
for Picture in PicturesArray:
    print Picture
    VkApi.wall.post(owner_id='YOUR_GROUP_ID_WITH_MINUS_IN_FRONT',attachments='photo'+str(Picture[0])+'_'+str(Picture[1]))
    time.sleep(random.randint(60,180))

"""
VkAdresses ->
paper.comics 21097
dob.rota 31230
iface 56634
evil_incorparate 60580
ilikes 80570

PublicStr ->
['paper.comics', '21097']
['dob.rota', '31230']
['iface', '56634']
['evil_incorparate', '60580']
['ilikes', '80570']
"""

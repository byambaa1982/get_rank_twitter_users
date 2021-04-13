# Sorting Twitter Users by Social Networking Potentials

![repo size](https://img.shields.io/github/repo-size/byambaa1982/get_rank_twitter_users)
![size](https://img.shields.io/github/languages/code-size/byambaa1982/get_rank_twitter_users)
![language count](https://img.shields.io/github/languages/count/byambaa1982/get_rank_twitter_users)
![social](https://img.shields.io/github/followers/byambaa1982?style=social)
![stats](https://img.shields.io/github/stars/byambaa1982/get_rank_twitter_users)


## Twitter API


All the information required to compute these metrics is accessible through the Twitter API 4
. An API
(Application Programming Interface) is a set of functions, protocols and tools that are used to build
an application, or to facilitate the communication with services. Twitter provides three kinds of API to
developers (two of them are public) that together provide access to information from the social network.
This information is obtained through different kind of requests, and it is useful for research, to search
for historical or real-time information, and to develop unofficial clients.
A measure based on simple metrics is the Social Networking Potential(SNP), defined as follows:

  ID  	 | Metric description    
-------- | ------------- | 
RT3      | Number of users who have retweeted author’s tweets
M4       | Number of users mentioning the author.  				
F1       | Number of followers.   

```math
SNP(i)=(Ir(i)+MR(i))/2
```

where the Interactor Ratio, Ir(i), and the Retweet and Mention Ratio, RMr(i), are defined as:

```math                               
Ir(i)=(RT3+M4/F1    and   RMr(i)=(#tweets of i retweeted + #tweets of i replied)/#tweets of i 
```

For each user, Ir(i) measures how many different users users interact with that user, while RMr(i) measures
how many of his tweets imply a reaction from the audience.
Note that the SNP measure considers all kind of actions on Twitter, except the favorites or likes. The
same occurs for a measure based on content and conversation, informally defined by Hatcher et al. [51].
The content criterion considers the number of published tweets and follow-up relationships, and it has
the 25% of the total importance. The conversation criterion considers the number of replies, as well as
the number of followers related with the user through mentions and retweets, and it has 75% of the total
importance of the measure.

      		

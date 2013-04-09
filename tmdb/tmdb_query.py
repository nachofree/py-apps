import json
import urllib2


URL = "http://api.themoviedb.org/3/"

class Tmdb:
    def __init__(self):
        self.key_string = "?api_key=661ca0798b0deda1a24f3572ca1a8abe"
        
    def doQuery(self):
        request = urllib2.Request(self.query, headers={"Accept" : "application/json"})
        f = urllib2.urlopen(request)
        response = f.read()
        f.close()
        
        return json.loads(response)



    def getUpcomingMovies(self):
        add_url = 'movie/upcoming'
        self.query = URL+add_url+self.key_string

    def searchByTitle(self, title):
        add_url = "search/movie"
        title_string = "&query="+title
        self.query = URL+add_url+self.key_string+title_string
        print self.query
        return self.doQuery()


        
def main():
    movie = Tmdb()
    results = movie.searchByTitle('inception')
    
    
    #the next line parses one value from that array
    print results['total_results']
if __name__=="__main__":        
    main()

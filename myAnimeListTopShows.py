
from bs4 import BeautifulSoup
import urllib.request
import colorama 
from colorama import Back , Fore, Style
import curses 
import time



topAll = "https://myanimelist.net/topanime.php"#link for the top 50 shows on MAL (My anime list) anime + movies
topManga ="https://myanimelist.net/topmanga.php" #link for the top 50 manga books on MAL 
topAnimeSeries = "https://myanimelist.net/topanime.php?type=tv"
topAiring = "https://myanimelist.net/topanime.php?type=airing"# link for top airing shows this season 
topUpcoming = "https://myanimelist.net/topanime.php?type=upcoming" #most anticipated new shows / seasons 
topAnimeMovies = "https://myanimelist.net/topanime.php?type=movie"
topOVA = "https://myanimelist.net/topanime.php?type=ova" 
topAnimePop = "https://myanimelist.net/topanime.php?type=bypopularity" #ranked based on popularity not user score

disp_upcoming = "Upcoming Anime shows "
disp_pop = " Anime series ranked by number of users"      
disp_anime = "Anime series of all time / user score "
disp_all_shows = "Anime Series and Anime movies "
disp_movies = "Anime Movies"
disp_ongoing = "Ongoing Anime series"
disp_manga = "Mangas "
disp_ova = " Original Video Animation"
def top(x, y , disp):
    url = urllib.request.urlopen(x) #we fetch the link using urllib 
    html_sample = url.read() #reading the website html content 
    
    soup = BeautifulSoup(html_sample, 'html.parser')#using the parser to get a bueatifulSoup object 
    soup.prettify()#the prettify method will give us a better and clearer formatting for our html 
    #with a separate line for each tag and each string .
    
    
    n = soup.find('a', attrs={
        'class' : 'link-blue-box next'
    })
    #looking for an anchor tag with the class named "link-blue-box next" to get the number of shows on the page 
    
    A = [int(s) for s in n.text.split() if s.isdigit()]
    # this works better than hard typing the value n = 50 as it can be changed later on if the website desides to update it 
    
    mangaList = soup.find_all('td', attrs={
        'class': y
    })
    #finding all the attributes in the page with the desired classname 
    print(Fore.CYAN + Style.BRIGHT + " °º¤ø,¸¸,ø¤º°`°º¤ø Top {} {} ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸".format(A[0], disp))
    print()
    i = 1 
    for x in mangaList : 
        #iterating through all the elements in the webpage 
        print(Fore.MAGENTA + Style.BRIGHT+'Rank {}'.format(i))
        print('===============================================')
        
        NeeData = x.text
        NeeData = NeeData.replace("Watch Episode Video", "")
        NeeData = NeeData.replace("Watch Promotional Video", "")
        print(Fore.MAGENTA + Style.BRIGHT + NeeData.strip())
        print()
        print()
        i += 1 
        
        
################### this next section was supposed to be a console menu with curses but I'm facing trouble doing it so you can uncomment and check if you want my 
#screen doens't want to update in vscode using python 3.9.1 and python 3.8.8 : tried both 


 
# obj = ['Top Anime Shows', 'Top Manga', 'Top Anime (shows/movies)', 'Top Anime Movies',
#            'Top Upcoming', 'Top Shows this season', 'Top OVA', 'Most Popular']  #our menu selected items 
    
# def display_obj(stdscr, line_index): 
#     stdscr.clear()
    
    
#     h, w = stdscr.getmaxyx()
#     for index , line in enumerate (obj): 
#         x = w//2 - len(line)//2 
#         y = h//2 - len(obj)//2 + index 
#         if index == line_index: 
#             stdscr.attron(curses.color_pair(1))
#             stdscr.addstr(y, x, line)
#             stdscr.attroff(curses.color_pair(1))
#         else : 
#             stdscr.addstr(y, x, line)
#     stdscr.refresh()
    
# def main(stdscr): 
#     #this is the setup for the static menu 
#     curses.curs_set(0)    
#     curses.init_pair(1, curses.COLOR_MAGENTA, curses.COLOR_WHITE)
#     line_index = 0
#     display_obj(stdscr, line_index)
    
#     #we set up how we navigate the menu object 
#     while 1 : 
#         key = stdscr.getch()
#         stdscr.clear()
#         if key == curses.KEY_UP and line_index > 0 : 
#             line_index -= 1 
#         elif key == curses.KEY_DOWN and line_index < len(obj)-1: 
#             line_index += 1 
#         elif key == curses.KEY_ENTER or key in [10, 13]: 
            
#             stdscr.refresh()
#             stdscr.getch()
#         display_obj(stdscr, line_index)
#         stdscr.refresh()

mangaClass = 'title al va-t clearfix word-break'
className = 'title al va-t word-break'
if __name__ == '__main__': 
    
    
    cond = True 
    while 1 : 
        print("****** MAL Scraper ******")
        print("1. Check top airing Anime Shows this season ")
        print("2. Top Anime Series / by user score")
        print("3. Top Upcoming ")
        print("4. Top Anime Movies")
        print("5. Top OVA ")
        print("6. Top of all time : Anime shows + movies ")
        print("7. Top Anime Shows by Popularity")
        print("8. Top Published Manga")
        print("0. Exit ")
        a = int(input(Fore.LIGHTMAGENTA_EX + Back.BLACK + "Pick you option here : "))
        
        if a == 1 : 
            top(topAiring, className, disp_ongoing)
        elif (a ==2): 
            top(topAnimeSeries, className, disp_anime)
        elif (a ==3):
            top(topUpcoming, className, disp_upcoming)
        elif (a ==4):
            top(topAnimeMovies, className, disp_movies)
        elif  (a == 5):
            top(topOVA, className, disp_ova)
        elif (a == 6): 
            top(topAll, className, disp_all_shows) 
        elif (a ==7): 
            top(topAnimePop, className, disp_pop)
        elif (a ==8):
            top(topManga, mangaClass, disp_manga)
        else : 
            b = (input("press (y|Y) for yes or (n|N) :"))
            if b in ['y','Y'] : 
                print(Fore.GREEN + '''
            `.--:://///++++++/////::--.`           
    `+oyhmmNNNNNMMMMMMMMMMMMMMMMMMNNNNNmmhyo+`    
    `MMMMMMMMMMMMMMmddddddddddmMMMMMMMMMMMMMM`    
     hMMMMhMMMMMMMMh.````````.hMMMMMMMMhMMMMh     
     -MMMM+/mMMMMMMMd-      -dMMMMMMMm/+MMMM-     
      yMMMN..sNMMMMMMN/    /NMMMMMMNs..NMMMy      
      `mMMMh` -hMMMMMMMy``yMMMMMMMh- `hMMMm`      
       -NMMMs   /mMMMMMMmmMMMMMMm/   sMMMN-       
        +MMMM+   `sNMMMMMMMMMMNs`   +MMMM+        
         oMMMM/    .hMMMMMMMMh.    /MMMMo         
          sMMMM/   `sMMMMMMMMs`   /MMMMs          
           oMMMM+ :mMMMMMMMMMMm: +MMMMo           
            +MMMMdMMMMMNooNMMMMMdMMMM+            
             :NMMMMMMNs`  `sNMMMMMMN:             
             :mMMMMMd.  ``  .dMMMMMm:             
           `yNMMMMMMNs./dd/.sNMMMMMMNy`           
           -MMMmo+NMMMmMMMMmMMMN+omMMM-           
           -Nd+.  -NMMMMMMMMMMN-  .+dN-           
           `-`  `:hMmNMMMMMMNmMh:`  `-`           
               .hMmo.-hMMMMh-.omMh.               
               /mo`    /mm/    `om/               
               .`       ``       `.
                      ''')
                time.sleep(2)
                exit()
            
    
    
    
    
 
        


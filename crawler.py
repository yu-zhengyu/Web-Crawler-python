##############################################################################
#  Control script that accepts user input for a keyword and crawling method  # 
#  then calls the corresponding crawler to begin crawling                    #
##############################################################################
import sys
import DFS_crawl
import BFS_crawl
import sendemail

def main():
	# Default keyword and crawling method
	keyword = "java"
	method = "dfs"
	information = ""

	if len(sys.argv) == 3:
		keyword = sys.argv[1]
		method = sys.argv[2]
	if method == "dfs":
		DFS_crawl.dfs_search(keyword)
	else:
		BFS_crawl.bfs_search(keyword)


if __name__ == '__main__':
	print "Do you want the routine send email tell you the routine is over?"
	print "Please input yes or no"
	issend = raw_input()
	if issend == 'yes':
		print 'Please input your gamil address:'
		username = raw_input()
		print 'Please input your password'
		psw = raw_input()
	main()
	if issend == 'yes':
		sendemail.sendemail(username, psw)

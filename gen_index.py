from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# for local hosting, since selenium requires a hosted page to work correctly
import http.server
import socketserver
import threading

from os import getcwd
# make it pretty
from bs4 import BeautifulSoup as bs
from prettierfier import prettify_html
import minify_html


# load the page in firefox-selenium and return the html
def load_page_firefox(page_name):
	from selenium.webdriver.firefox.options import Options
	options = Options()
	options.headless = True
	options.log.level = "fatal"
	driver = webdriver.Firefox(options=options, executable_path=getcwd() + '\\geckodriver.exe')
	driver.get(page_name)
	try:
		WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "prerendered")))
	except TimeoutException as err:
		print(err)
		exit(-1)
	html = driver.find_element_by_tag_name('html').get_attribute('outerHTML')
	driver.quit()
	return html


# make some modifications to the page
def update_page(soup):
	meta1 = soup.new_tag('meta')
	meta1['name'] = 'description'
	meta1['content'] = 'PoE Gwennen regex generator.'
	meta2 = soup.new_tag('meta')
	meta2['name'] = 'keywords'
	meta2['content'] = 'best videogames, free to play, free game, online games, fantasy games, PC games, PC gaming, Genshin Impact, character planner'
	soup.head.extend([meta1, meta2])
	soup.find('meta', {'name': 'robots'}).extract()
	soup.find('script', {'src': 'gen_page.py'})['src'] = 'main.py'


def main():
	# where is the server
	port = 62435
	handler = http.server.SimpleHTTPRequestHandler
	server = socketserver.TCPServer(("", port), handler)
	thread = threading.Thread(target=server.serve_forever)
	thread.daemon = True  # so the server dies when the program exits
	thread.start()
	local_page = f'http://localhost:{port}/dynamic_page.html'

	html = load_page_firefox(local_page)
	server.shutdown()  # kill the server since we are done with it
	soup = bs(html, "html.parser")
	update_page(soup)
	try:
		minified = minify_html.minify(str(soup), minify_js=False, minify_css=False)
		with open('index.html', 'w', encoding='utf-8') as f:
			f.write(f"<!DOCTYPE html>{minified}")
	except SyntaxError as e:
		print(e)


if __name__ == '__main__':
	main()

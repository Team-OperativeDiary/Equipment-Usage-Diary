from multiprocessing import Process
from main_website.app import app as main_website_app
from redirected_website.app import app as redirected_website_app

def run_main_website():
    main_website_app.run(debug=True, use_reloader=False)

def run_redirected_website():
    redirected_website_app.run(debug=True, port=5001, use_reloader=False)

if __name__ == '__main__':
    main_website_process = Process(target=run_main_website)
    redirected_website_process = Process(target=run_redirected_website)

    main_website_process.start()
    redirected_website_process.start()

    main_website_process.join()
    redirected_website_process.join()

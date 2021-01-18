# WDSSIgLandingPage made with ReactJS, HTML/CSS and Jquery
DEMO: <a href="https://wdssiglandingpage.netlify.app">Demo from personal git account</a>
## To Run it:

### 1. For development
To build this website, you will need to have Node >=6 downloaded and installed on your machine. You can get it <a href="https://nodejs.org/en/download/">here</a>
### 2. Build a Create-React-App
Run `npx create-react-app yourappname`
When the app building is finished run `cd yourappname` and run `npm start` to test it out.
Hit ctrl+c in the terminal when you want to stop the server.
For this project you will also need to install JQuery, ReactGA and ts-particles do this by running `npm install jquery --save` ,`npm install react-ga --save` and `npm install react-particles-js --save` in your terminal while inside your project folder.
### 3. Download the template
Once you have a React app up and running by following the steps above, download the code and replace the "public" and "src" folders of your newly built app with that you just downloaded.
### 4. Making Changes
Running `npm start` again will get you the website.
### 5. Updating the posts and json file.
Run the python file IN ITS CURRENT DIRECTORY to update the posts and the html. This is still a janky solution but it works for now. The IG Api access tokens have expired due to non use. Use this <a href="https://developers.facebook.com/docs/instagram-basic-display-api/getting-started">guide</a> to create a facebook developer account and create your own tokens. Update the `access_token` variable in `public/LandingPage.py`
  
### 6. Deploying
Ive tested deploying on Netlify, works fine, except the browser caches older versions sometimes so need to find a solution for that, i recommend using Netlify as react seems to not work using GitHub pages, or I just couldnt make it work
### 7. Dependencies
##### React Dependencies
- react-ga 
> `npm install react-ga --save`
- jquery 
> `npm install jquery --save`
- react-particles-js
>`npm install react-particles-js`
##### Python Dependencies
- requests
> `pip install requests`
- BeautifulSoup4
> `pip install beautifulsoup4`

## Credits
##### Udemy Course
<a href="https://www.udemy.com/projects-in-reactjs-the-complete-react-learning-course/learn/v4/overview">Projects in ReactJS: The Complete React Learning Course by Eduonix</a>

##### Stackoverflow
(obviously, how else would I learn all this in such a short time) You get significantly better at googling down the line of programming lol.

# 1. Subaru Weather Application Website 🌐

The website was designed as a Single Page Application (SPA). It was designed to be expandable and component-based such that it should be easily modifiable if it needs a few changes.  

## 1.1. Overview

### 1.1.1. Features

Tracking sensor values should be as easy as adding an entry to a settings file. The website should be seamlessly resizable, and the elements of the website should reconfigure where each element will stack on each other if the elements run out of horizontal space.  

### 1.1.2. Design

The Single Page design was selected as it best suited to display a swath of information at once; the framework allows for dynamic pages and fast webpage load times. The react framework was chosen for this reason. The react framework uses an extension for JavaScript called JSX; the extension allows for the use of XML-like tags; this system is very extensible, and compatible with native HTML tags.

For the UI framework of the website, I had initially considered using MDL then Material-UI. MDL, although lightweight as a framework, had stopped seeing updates and was too limited in capabilities. Material-UI was easy to use, although it was full of issues and bugs. I have settled to use Semantic-UI as it looked sleek and was easy to use compared to the other libraries.  

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## 1.2. Available Scripts

In the project directory, you can run:

### 1.2.1. `npm start`

Runs the app in the development mode.<br>
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.<br>
You will also see any lint errors in the console.

### 1.2.2. `npm test`

Launches the test runner in the interactive watch mode.<br>
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### 1.2.3. `npm run build`

Builds the app for production to the `build` folder.<br>
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.<br>
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### 1.2.4. `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can’t go back!**

If you aren’t satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (Webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you’re on your own.

You don’t have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn’t feel obligated to use this feature. However we understand that this tool wouldn’t be useful if you couldn’t customize it when you are ready for it.

## 1.3. Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### 1.3.1. Code Splitting

This section has moved here: https://facebook.github.io/create-react-app/docs/code-splitting

### 1.3.2. Analyzing the Bundle Size

This section has moved here: https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size

### 1.3.3. Making a Progressive Web App

This section has moved here: https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app

### 1.3.4. Advanced Configuration

This section has moved here: https://facebook.github.io/create-react-app/docs/advanced-configuration

### 1.3.5. Deployment

This section has moved here: https://facebook.github.io/create-react-app/docs/deployment

### 1.3.6. `npm run build` fails to minify

This section has moved here: https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify

## Code Documentation

The website was designed in a component-based way. Each part of the website is scripted to represent a component and components that are composed of other components. Each component has state and props. Put simply, props represent the "initial state" of the component and the state represents the variable data that can change within the system.  

For more information, read the react documentation.  
https://reactjs.org/

### Update homepage location `Git/swa/website/package.json`
Make sure to update the website's homepage location when moving the location of the website itself. The website needs to be able to refer to itself. Change the following line to reflect the changes.

```json
"homepage": "http://shell/~genzo/Weather/",
```

### Example addition of a figure or plot

The addition of a graph to the website is done in two parts. First, an entry must be made for the collection and creation of the figure. This is done by editing `Settings.ini` for the Figurebot. Then, after the addition of the new plot, the created image must be displayed through the editing of the json file, `graphs.json`, that keeps track of the website's cards.

#### `Settings.ini` - Settings file for the creation of graphs and collection of data `Git/swa/figurebot/Settings.ini`

```ini
   [ENVOY.SENSOR.F3]                     # Figure Identifier [ENVOY.SENSOR.<FIGURE#>]
    Title         = Atmospheric Pressure # Label for the title of the figure
    TitleFontsize = 16                   # Font size for the title of the figure
    XAxisLabel    = Time                 # Label for the X-axis of the figure
    YAxisLabel    = Atm                  # Label for the Y-axis of the figure
    DateFormat    = %%I:%%M:%%S %%p      # Format for the date/time labels for the data
    SizeX         = 16                   # Horizontal size of the figure in dimensions.
    SizeY         = 9                    # Vertical size of the figure in dimensions.
    Dpi           = 100                  # Resolution of the figure.

    [ENVOY.SENSOR.F3.P0]             # Plot Identifier [ENVOY.SENSOR.<FIGURE#>.<PLOT#>]
        Label = Atmospheric Pressure # Legend label for this plot
        RequestString = TSCL.ATOM    # Tsc status alias
        Granularity = 1440           # Maximum number of stored data points
```

#### `graphs.json` - Card data for the website `Git/swa/website/public/data/graphs.json`
```json
{
    "src": "./images/Atmospheric Pressure.png",                     # Filepath should match the generated image's filepath
    "alt": "Atmospheric Pressure plot of the last 24 hours",        # Alternative text in case of no image.
    "href": "./images/Atmospheric Pressure.png",                    # Link to the image itself.
    "header": "Atmospheric Pressure plot of the last 24 hours.",    # Header of the card that is displayed on the website.
    "mouseover": "Atmospheric Pressure plot of the last 24 hours.", # [UNUSED] Mouseover text.
    "description": "Atmospheric Pressure plot of outside conditions on the catwalk of Subaru Telescopes for the last 24 hours." # Description of the card displayed on the website.
}
```

Run these commands to build the website, create the plots, and then move the files for deployment.

```bash
$ make cleanall; make
$ bash Master.sh
```
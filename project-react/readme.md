# React Insight
1. Create a function like function App() {}

2. Create a variable and assign a value to it like
let counter = 15...create a state with useState method which returns 2 values in the form of an array [the variable counter, the method setCounter]like const [counter, setCounter] = useState()

const [counter, setCounter] = useState(15)
const addValue = () => {
    setCounter(counter +1)
}
NB: setCounter((prevcounter) => prevcounter +1)
The principole behind.

NB: setCounter((prevcounter) => prevcounter +1)
    setCounter((prevcounter) => prevcounter +1)
    setCounter((prevcounter) => prevcounter +1)
The bactch principle behind React which increase by 3

3. Create a function call App() and let it return 
HTML elements like H1, H2 or Buttons to be displayed on the page

4. Varriable injection (creating a variable like
let counter = 15) and insert it in the return in the HTML to be display {counter}

5. Set an onClick method with a connection value like onlick={addValue} for buttons and create a function to respond to the button like 
const addValue = () => (15)

6. React: Provides a mechanism to update anything and everything on a webpage by proving a concept call STATE which is constantly being moinitored and any change in it rerenders the UI on the webpage and this is what the state is being designed


7. Reconcilliation: Diff one tree with another to determine which parts needs to be changed.(Diff Algorithms)--Virtual DOM and the Real DOM
And here the setState(useState Method is used to rerender)
NB: When an App is updated usually through setState, a new tree is generated. The new tree is diffed with the previous tree to compute which operations are needed to update the rendered app.

8. Reconciliation Vs Rendering 
The reason it can support so many targets is bcos React is designed so that reconcilliation and rendering are separate phases. The reconciler does the work of computing which parts of a tree have changed; the renderer then uses that information to actually update the rendered app

This separation means that React DOM and React Native can use their own renderers while sharing the same reconciler, provided by React core.

9. Fiber Time stamp(2:1)

10. Setting up React

11. Setting up Vite-Tailwind
    1. run npm create vite@latest
    2. set project's name
    3. select framework eg. React
    4. Then select a variant eg.JavaScript
    5. then change directory to the project folder and run npm install/i to install the vite packages
    6. Go to tailwindcss.com, docs to follow the process invovled in installing tailwindcss
        i. Install Tailwind CSS by running the following
        (npm install -D tailwindcss postcss autoprefixer
        npx tailwindcss init -p)
        
        ii. Configure your template path (Add the paths to all of your template files in your tailwind.config.js file.) This...
        /** @type {import('tailwindcss').Config} */
        export default {
          content: [
            "./index.html",
            "./src/**/*.{js,ts,jsx,tsx}",
          ],
          theme: {
            extend: {},
          },
          plugins: [],
        }

        iii. Add the Tailwind directives to your CSS(index.css)
        (Add the @tailwind directives for each of Tailwind’s layers to your ./src/index.css file.) This ...
             @tailwind base;
             @tailwind components;
             @tailwind utilities;

12. Read on: useCallBack, useEffect, useSate,    useRef, Memorization technique, customisedHooks(desinging our own hooks), Reuseability of components
    
    https://react.dev/reference/react/useCallback




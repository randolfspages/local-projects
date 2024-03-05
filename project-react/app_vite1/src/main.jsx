import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'


const reactElement = {
    type: 'a',
    props: {
        href: 'https://google.com',
        target: '_blank'
    },
    children: 'Click me to visit google'
}

const rElement = React.createElement(
    'a',
    {href: '', target:'_blank'},
    'Click to visit google'
)

function Myapp() {
    return (
        <div>
            <h1>Custom React App</h1>
        </div>
    )
}


const AnotherElement = (
    <a href="https://google.com" target='_blank'>Visit Google</a>
)

ReactDOM.createRoot(document.getElementById('root')).render(
 
    App()

)

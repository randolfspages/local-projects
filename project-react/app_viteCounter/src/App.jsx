import { useState } from 'react'

import './App.css'

function App() {
 
  //let counter = 15
  const [counter, setCounter] = useState(15)

  const addValue = () => {
    setCounter(counter + 1)
  }

  const reduceValue = () => {
    setCounter(counter - 1)
  }

  return (
    <>
      <h1>React Crash Course {counter}</h1>
      <h2>Counter Value: {counter}</h2>
      <button onClick={addValue}>Add Value</button>{' '}
      <button onClick={reduceValue}>Decrease Value</button>
      <p>footer: {counter}</p>
    </>
  )
}

export default App

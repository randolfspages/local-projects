import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Card from './components/card'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <h1 className='text-3xl bg-green-500 p-3 rounded-md'>Professionals' Profile</h1>
      <Card username='Java James' post='Software Engineer' image="https://images.pexels.com/photos/18681384/pexels-photo-18681384/free-photo-of-gaming.jpeg?auto=compress&cs=tinysrgb&w=600&lazy=load"/>
      <Card username='Json Jon' post='Software Engineer' image="https://images.pexels.com/photos/18264716/pexels-photo-18264716/free-photo-of-man-in-headphones-showing-programming-process-on-a-laptop.jpeg?auto=compress&cs=tinysrgb&w=600&lazy=load"/>
      <Card username='Python Peter' post='Software Engineer' image="https://images.pexels.com/photos/18681382/pexels-photo-18681382/free-photo-of-coding.jpeg?auto=compress&cs=tinysrgb&w=600&lazy=load"/>
    </>
  )
}

export default App

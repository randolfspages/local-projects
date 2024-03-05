import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [color, setColor] = useState('olive')
    
  
  return (
      <div className='w-full h-screen duration-200' style ={{backgroundColor:color}}>
            <div className='flex flex-auto justify-center'>
              <h1 className='text-white' style={{fontSize:30, fontWeight:800, padding:20}}>Background Color Changer App.</h1>
            </div>
            <div className='fixed flex flex-wrap justify-center bottom-12 inset-x-0 px-2'>
                <div className='flex flex-wrap gap-3 shadow-lg bg-white px-3 py-2 rounded-3xl justify-center max-w-2xl'>
                    <button onClick={() => setColor('red')} className='outline-none px-4 py-1 rounded-full text-black shadow-lg' style={{backgroundColor:'red', color:'white'}}>Red</button>
                    <button onClick={() => setColor('green')} className='outline-none px-4 py-1 rounded-full text-black shadow-lg' style={{backgroundColor:'green', color:'white'}}>Green</button>
                    <button onClick={() => setColor('gray')} className='outline-none px-4 py-1 rounded-full text-black shadow-lg' style={{backgroundColor:'gray', color:'white'}}>Gray</button>
                    <button onClick={() => setColor('black')} className='outline-none px-4 py-1 rounded-full text-black shadow-lg' style={{backgroundColor:'black', color:'white'}}>Black</button>
                    <button onClick={() => setColor('brown')} className='outline-none px-4 py-1 rounded-full text-black shadow-lg' style={{backgroundColor:'brown', color:'white'}}>Brown</button>
                  
                </div>
            </div>
      </div>
  )
}

export default App

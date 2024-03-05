import React from 'react'

function Card({username='Not assigned yet', post='Not assigned yet',
image='No image yet'}) {
  return (
    <div>
        
        <figure className="md:flex bg-slate-100 md:p-0 mt-3 rounded-xl p-8 dark:bg-slate-800">
                <img className="w-40 h-40 md:h-auto md:rounded-none md:w-auto md:pr-5 rounded-full mx-auto" src= {image} alt="" width="384" height="512"/>
            <div className="pt-6 text-center space-y-4">
                <blockquote>
                    <p className="text-lg font-medium md:text-left">
                        “Tailwind CSS is the only framework that I've seen scale
                        on large teams. Its easy to customize, adapts to any design,
                        and the build size is tiny.”
                    </p>
                </blockquote>
            <figcaption className="font-medium md:text-left">
                <div className="text-sky-500 dark:text-sky-400">
                    {username}
                </div>
                <div className="text-slate-700 dark:text-slate-500 md:text-left">
                    {post}
                </div>
            </figcaption>
        </div>
        </figure>
        
    </div>
  )
}

export default Card

'use client'
import Link from 'next/link'
import { useState } from 'react'
export default function Nav (){
    const [nav , setNav] = useState(false)
    const handleClick = () => {
        setNav(!nav)
    }

    return(
      <>
      <header className='flex justify-between w-screen h-16  text-white items-center   fixed z-40 bg-transparent'>
        <nav className='flex md:justify-between w-screen items-center'>
        <div className=' text-lg md:text-xl  font-semibold z-50 ml-4'>
        <Link href="/" className=' z-50' >Notas</Link>
        </div>
        <ul className={`flex flex-col font-extrabold justify-center  items-center absolute bg-white md:bg-transparent w-screen h-screen  z-50 gap-4 text-xl md:text-xs  transition-all duration-300 md:flex-row md:relative md:w-fit md:h-fit ${nav ? "closeNav" : "openNav"}`}>
        <li className=''> 
            <Link href="/" onClick={handleClick} className='hover:text-lime-500'>
              title 1
              </Link>
        </li>
            <li>  
            <Link href="/" onClick={handleClick} className='hover:text-lime-500'>    
            title 2
            </Link>  
        </li>
          
        <li> 
            <Link href="/" onClick={handleClick} className='hover:text-lime-500'>
          title 3
              </Link>
        </li>
        <li>
        <Link href="/" onClick={handleClick} className='hover:text-lime-500'>
          title 4
              </Link>
          </li>
          <li className='block md:hidden '>
            <Link href="/Todas-Las-Recetas" onClick={handleClick} className=''>
              Iniciar Sesion
            </Link>
            </li>
        </ul>
        <span className='hidden md:block mr-4'>
            Iniciar Sesion
        </span>
      </nav>
      <div className='menu block text-black z-50 mr-10  cursor-pointer md:hidden ' onClick={handleClick}>
          <div className='h-1 w-10 bg-black rounded'></div>
          <div className='h-1 w-10 mt-1.5 bg-black rounded'></div>
          <div className='h-1 w-10 mt-1.5 bg-black rounded'></div>
        </div>
      </header>
      </>
    )
}
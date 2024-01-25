import Image from "next/image"
import ImagenHero from '../../../public/Images/Hero.jpg'
export default function Hero() {
    return(
        <>
        <section className="hero-container text-white  flex p-2 pt-20 md:pt-0 flex-col md:flex-row justify-center items-center min-h-[600px] gap-10">
            <div className="hero-text">
                <h1 className="text-3xl text-lime-600 m-4">Lorem ipsum dolor sit amet, consectetur adipisicing elit.</h1>
                <p className="m-4">Lorem ipsum dolor sit amet consectetur adipisicing elit. Ipsum, odit.</p>
                <button className="bg-lime-600 p-4 m-4 rounded">MI PRIMERA NOTA</button>
            </div>
        <Image
        width={400}
        height={400}
        src={ImagenHero}
        alt="hero-image"
        className="max-h-[400px] object-cover p-4  border-solid border-lime-600 border-4"
        ></Image>
        </section>
      </>
    )
}
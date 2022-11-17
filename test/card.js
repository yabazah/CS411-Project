import React , { useState, useEffect}from 'react'
import '../card.css'
import Card from 'react-tinder-card'
import Icon  from '../assets/icon.jpg'
import axios from "./axios"



export default function Cards() {
const [product, setProduct] = useState([])

useEffect(()=>{
    const fetchData = async () =>{
        const req = await axios.get('/card')
        setProduct(req.data)
        console.log(product)
           }
           fetchData()
    
},[product.name])

const swiped =(direction, nametodelete)=>{
    console.log( `removing ${nametodelete}`)
}  

const outOfFrame =(name)=>{
    console.log( ` ${name}  left the screen`)
}
  return<div className='Cards'>
    <div className="cards_container">        
    {
            product.map((item)=>{
               
                return <Card
                    className='swipe'
                    key={item._id}
                    preventSwipe={["up", "down",]}
                    onSwipe ={(dir)=>swiped(dir, item.name)}
                    onCardLeftScreen={()=>outOfFrame(item.name)}
                    >
                        <div style={{
                         backgroundImage: `url(${item.image})`,
                        }}
                        className ='card'
                        >
                            <h3>{item.name}</h3>
                        </div>
                       
                    </Card>
             
                        
            })
        }
          

    </div  >

   
     
    </div>

}
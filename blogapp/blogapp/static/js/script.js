// ! BACKGROUND COLOR CHANGE WITH THE ICONS ON RIGHT SIDE OF NAVBAR ! \\

const changeColor = document.getElementById('toggleDark')

const body = document.querySelector('body')

changeColor.addEventListener('click', function(){

    this.classList.toggle('bi-moon')


    if(this.classList.toggle('bi-emoji-sunglasses')){

        body.style.background ='white'

    }else{

        body.style.background ='darkgray'

    }

})


// ! BACKGROUND STAR ANIMATION THAT IS ON THE LANDING PAGE ! \\

for(let i=1 ; i<=1050 ; i++){

    let stars = document.createElement('div')

    stars.classList.add('star')

    let size = Math.random()*10

    stars.style.fontSize = 2 + size+'px'

    stars.style.left = Math.random()* + innerWidth + 'px'

    stars.style.top = Math.random()* + innerHeight + 'px'

    stars.style.filter = `hue-rotate(${i * 25}deg)`

    document.querySelector('.sec').appendChild(stars)

}


function animateYıldız(){
    
    let AllStars = document.querySelectorAll('.star')


    let num = Math.floor(Math.random()*AllStars.length)

    AllStars[num].classList.toggle('animate')

}

setInterval(animateYıldız,1)
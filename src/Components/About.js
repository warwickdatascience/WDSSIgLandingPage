import React, { Component } from 'react';
import Particles from 'react-particles-js';

class About extends Component {
  render() {

    if(this.props.data){
      var name = this.props.data.name;
      var profilepic= "images/"+this.props.data.image;
      var bio = this.props.data.bio;
    }

    return (
      <section id="about">
	  <Particles
        id="tsparticles"
        params={{
          fpsLimit: 144,
          interactivity: {
            detectsOn: "window",
            events: {
              onClick: {
                enable: true,
                mode: "push",
              },
              onHover: {
                enable: false,
                mode: "bubble",
              },
              resize: true,
            },
            modes: {
              bubble: {
                distance: 150,
                duration: 2,
                opacity: 1,
                size: 0.1,
              },
              push: {
                quantity: 1,
              },
            },
          },
          particles: {
            color: {
              value: ["#ffffff","#11abb0"],
            },
            links: {
              color: ["#ffffff","#11abb0"],
              distance: 150,
              enable: true,
              opacity: 0.2,
              width: 0.01,
            },
            collisions: {
              enable: true,
            },
            move: {
              direction: "none",
              enable: true,
              outMode: "bounce",
              random: false,
              speed: 0.75,
              straight: false,
            },
            number: {
              density: {
                enable: true,
                value_area: 1000,
              },
              value: 100,
            },
            opacity: {
              value: 1,
			  anim: {
	                enable: true,
	                speed: 2,
	                opacity_min: 0.01,
	            },
            },
            shape: {
              type: "circle",
            },
            size: {
              random: false,
              value: 1.5,
            },
          },
          detectRetina: true,
        }}
      />
      <div className="row">
         <div className="three columns">
            <img className="profile-pic"  src={profilepic} alt="WDSS Logo" />
         </div>
         <div className="nine columns main-col">
            <h2>{name}</h2>
            <p>{bio}</p>
         </div>
      </div>

   </section>
    );
  }
}

export default About;

import React, { Component } from 'react';

class Overlays extends Component {
	
  render() {
	
    if (this.props.data){
      var overlays = this.props.data.posts.map(function(overlays) {
	var links = overlays.category.split(',');
	return <div className="overlayContainer" id={"m" + overlays.id} style={{display: 'none'}}>
          <div className="overlayImage" style={{backgroundImage: 'url(../images/portfolio/' + overlays.id + '.png)'}}></div>
	  <div className="overlayComments">
	    <div className="overlayCaption">
              <p>{overlays.caption}</p>
              <p>{overlays.timestamp}</p>
	      <div className="links">
                {
		  links.map(link => (
		    <div>
	              <a href={link}>
		        {link}
		      </a>
		    </div>
		  ))
		}
	      </div>
	    </div>
          </div>
          <button className="closeOverlayButton" id={"b" + overlays.id}>
	    CLOSE
          </button>
        </div>
      })
    }

    return (
      <section id="overlays">

        <div className="overlayToggle" id="overlayToggle" style={{display: 'none'}}>
	  <div className="overlayBG"></div>
	  <div className="overlay">
	    {overlays}
  	  </div>
        </div>
      </section>
    );
  }
}	
	    
export default Overlays;

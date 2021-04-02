import React, { Component } from 'react';

class Footer extends Component {
  render() {
	  
	if(this.props.data){
	  var networks= this.props.data.social.map(function(network){
        return <li key={network.name}><a href={network.url}><i className={network.className}></i></a></li>
      })
	  var year = this.props.data.currentYear;
    }

    return (
      <footer>

     <div className="row">
        <div className="twelve columns">
		   <ul className="social-links">
		   {networks}
           </ul>
		   <a href="https://www.wdss.io" className="address">Warwick Data Science Society {year}</a>
        </div>
        <div id="go-top"><a className="smoothscroll" title="Back to Top" href="#about"><i className="icon-up-open"></i></a></div>
     </div>
  </footer>
    );
  }
}

export default Footer;

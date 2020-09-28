import React, { Component } from 'react';

class Portfolio extends Component {
	
  render() {
	
    if(this.props.data){
      var posts = this.props.data.posts.map(function(posts){
        var postImage = 'images/portfolio/m'+posts.image;
	  return <div key={posts.title} className="columns portfolio-item">
           <div className="item-wrap">
            <a id={posts.title} role="button" title={posts.title}>
               <img alt={posts.title} src={postImage} />
               <div className="overlay">
                  <div className="portfolio-item-meta">
					<h5>{posts.title}</h5>
					<p>{posts.category}</p>
					  <button id={posts.title} className="overlayButton"></button>
                  </div>
                </div>
            </a>
          </div>
        </div>
      })
    }

    return (
      <section id="portfolio">

      <div className="row">

         <div className="twelve columns collapsed">

            <div id="portfolio-wrapper" className="bgrid-quarters s-bgrid-thirds cf">
                {posts}
            </div>
          </div>
      </div>
   </section>
    );
  }
}

export default Portfolio;

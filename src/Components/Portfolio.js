import React, { Component } from 'react';

class Portfolio extends Component {
	
  render() {
	
    if(this.props.data){
      var posts = this.props.data.posts.map(function(posts){
        var postImage = 'images/portfolio/'+posts.id+'.png';
	var links = posts.category.split(',');
	if (links.length == 1 && links[0] != "") {
	  return <div key={posts.title} className="columns portfolio-item">
           <div className="item-wrap">
            <a id={posts.id} role="button" title={posts.caption.substr(0,100) + "..."} href={links[0]} target="_blank">
               <img alt={posts.caption.substr(0,100) + "..."} src={postImage} />
                <div className="overlay">
                  <div className="portfolio-item-meta">
	      		<h5>{posts.caption.substr(0,100)}...</h5>
			<button id={posts.id} className="overlayButton" style={{ display: "none" }}></button>
                  </div>
                </div>
            </a>
          </div>
        </div>
      }
	else {
		return <div key={posts.title} className="columns portfolio-item">
           <div className="item-wrap">
            <a id={posts.id} role="button" title={posts.caption.substr(0,100) + "..."}>
               <img alt={posts.caption.substr(0,100) + "..."} src={postImage} />
               <div className="overlay">
                  <div className="portfolio-item-meta">
		      <h5>{posts.caption.substr(0,100)}...</h5>
			<button id={posts.id} className="overlayButton" style={{ display: "none" }}></button>
                  </div>
                </div>
            </a>
          </div>
        </div>
	}
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

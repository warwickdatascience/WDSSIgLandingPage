import React from 'react';
import ReactGA from 'react-ga';
import $ from 'jquery';
import Overlays from './Components/Overlays';

class Overlay extends React.Component {

  constructor(props){
    super(props);
    this.state = {
      resumeData: {}
    };

    ReactGA.initialize('UA-110570651-1');
    ReactGA.pageview(window.location.pathname);

  }

  getResumeData(){
    $.ajax({
      url:'/resumeData.json',
      dataType:'json',
      cache: false,
      success: function(data){
        this.setState({resumeData: data});
      }.bind(this),
      error: function(xhr, status, err){
        console.log(err);
        alert(err);
      }
    });
  }

  componentDidMount(){
    this.getResumeData();
  }

  render() {
    return (
      <div className="Overlay">
	<Overlays data={this.state.resumeData.portfolio}/>
      </div>
    );
  }
}

export default Overlay;

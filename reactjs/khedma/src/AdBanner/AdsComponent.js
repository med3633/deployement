// AdsComponent.js
import React, { Component } from 'react';



class GoogleAds extends Component {

  componentDidMount() {
      (window.adsbygoogle = window.adsbygoogle || []).push({});
  }

  render() {
      return (
              <ins className='adsbygoogle'
                  style={{ display: 'block' }}
                  data-ad-client= 'ca-pub-2368877069845725'
                  data-ad-slot={this.props.slot}
                  data-ad-format= 'auto'
                  data-full-width-responsive="true"
              >
              </ins>
      );
  }
}

export default GoogleAds;

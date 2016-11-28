import React from "react";

import PageNavButton from "./PageNav/PageNavButton"

export default class PageNav extends React.Component {

  render() {
    var prev_button;
    var next_button;
    if (this.props.prev_page) {
      prev_button = <PageNavButton
                     handleClick={this.props.handlePageTransition}
                     displayText="Previous"
                     pageValue={this.props.prev_page}/>
    }
    if (this.props.next_page) {
      next_button = <PageNavButton
                     handleClick={this.props.handlePageTransition}
                     displayText="Next"
                     pageValue={this.props.next_page}/>
    }
    return (
      <nav aria-label="...">
        <ul className="pager">
          {prev_button}
          {next_button}
        </ul>
      </nav>
    );
  }
}

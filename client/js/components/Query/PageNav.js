import React from "react";

import PageNavButton from "./PageNav/PageNavButton";

export default class PageNav extends React.Component {

  render () {
    var prevButton;
    var nextButton;
    if (this.props.prev_page) {
      prevButton = (<PageNavButton
                     handleClick={this.props.handlePageTransition}
                     displayText="Previous"
                     pageValue={this.props.prev_page}/>);
    }
    if (this.props.next_page) {
      nextButton = (<PageNavButton
                     handleClick={this.props.handlePageTransition}
                     displayText="Next"
                     pageValue={this.props.next_page}/>);
    }
    return (
      <nav aria-label="...">
        <ul className="pager">
          {prevButton}
          {nextButton}
        </ul>
      </nav>
    );
  }
}
PageNav.propTypes = {
  handlePageTransition: React.PropTypes.function.required,
  next_page: React.PropTypes.int.required,
  prev_page: React.PropTypes.int.required
};

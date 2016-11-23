import React from "react";

import PageNavButton from "./PageNav/PageNavButton"

export default class PageNav extends React.Component {

  find_starting_point(){
    var num_buttons = this.props.num_buttons;
    var page = this.props.page;
    var max_page = this.props.max_page;
    if (num_buttons > max_page){
      num_buttons = max_page;
    }
    var start_point = page - Math.floor(num_buttons / 2);
    if (start_point > (max_page - num_buttons)) {
      start_point = (max_page - num_buttons);
    }
    start_point = start_point >= 1 ? start_point : 1;
    return start_point;
  }

  render() {
    var total_buttons_desired = 7
    var nav_buttons = [];
    if (this.props.max_page > 1){
      var start_point = this.find_starting_point()
      for (var i = 0; i < this.props.num_buttons; i++){
        var working_page = start_point + i;
        var displayText = working_page;
        var pageValue = working_page;
        var active = (working_page == this.props.page)
        var done = false;
        if (i == 0){
          displayText = "First";
          pageValue = 1;
          done = false;
        }
        else if (i == this.props.num_buttons - 1 || working_page == this.props.max_page ){
          displayText = "Last";
          pageValue = this.props.max_page;
          done = true;
        }
        nav_buttons.push(<PageNavButton
                          key={i}
                          active={active}
                          handleClick={this.props.handlePageTransition}
                          displayText={displayText}
                          pageValue={pageValue}/>);
        if (done) {
          break;
        }
      }
    }
    return (
      <nav aria-label="Page navigation">
        <ul className="pagination">
        { nav_buttons.map(function(object, i){
           return object;
         })}
        </ul>
      </nav>
    );
  }
}

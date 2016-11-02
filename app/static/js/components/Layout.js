import React from "react";

import Query from "./Query"
import Footer from "./Footer"

export default class Layout extends React.Component {

  render() {
    return (
      <div>
        <Query />
        <Footer />
      </div>
    );
  }
}

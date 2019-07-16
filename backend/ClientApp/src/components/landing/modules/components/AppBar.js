import React from 'react';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import MuiAppBar from '@material-ui/core/AppBar';

const styles = theme => ({
  root: {
    color: "#4dd0e1",
  },
});

function AppBar(props) {
  return <MuiAppBar elevation={0} position="static" {...props} color="#4dd0e1"/>;
}

AppBar.propTypes = {
  classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(AppBar);

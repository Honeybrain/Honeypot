import '../../styles.css';
import BlockIpWidget from './widgets/BlockIpWidget';
import LogViewerWidget from './widgets/ListConnectionsWidget';
import ContainerMonitorWidget from './widgets/ContainerMonitorWidget';
import { Grid } from '@mui/material';
import { DashboardProvider } from '@providers/DashboardProvider';

const Dashboard = () => {
  return (
    <DashboardProvider>
      <Grid container direction="column" style={{ height: '100%' }}>
        <Grid item container>
          <Grid item xs={4}>
            <ContainerMonitorWidget />
          </Grid>
          <Grid item xs={4}>
            <BlockIpWidget />
          </Grid>
        </Grid>
        <Grid item style={{ flexGrow: 1 }}>
          <LogViewerWidget />
        </Grid>
      </Grid>
    </DashboardProvider>
  );
};

export default Dashboard;

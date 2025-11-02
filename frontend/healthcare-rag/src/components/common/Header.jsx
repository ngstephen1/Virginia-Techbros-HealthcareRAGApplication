import React from 'react';
import { AppBar, Toolbar, Typography, Button, Container, Box } from '@mui/material';
import AddIcon from '@mui/icons-material/Add';
import { MAX_DOCUMENTS } from '../../config/theme';

const Header = React.memo(({ uploadedCount, startNewConversation }) => (
  <AppBar position="static" color="default" sx={{ bgcolor: 'white', borderBottom: 1, borderColor: 'grey.300', boxShadow: 'none' }}>
    <Container maxWidth="md">
      <Toolbar disableGutters sx={{ justifyContent: 'space-between' }}>
        <Box>
          <Typography variant="h5" component="div" color="primary.main" fontWeight={600}>
            ResearchBot
          </Typography>
          <Typography variant="caption" color="text.secondary">
            AI Literature Analysis Assistant
          </Typography>
        </Box>
        <Box sx={{ display: 'flex', alignItems: 'center', gap: 2 }}>
          <Typography variant="body2" color="text.secondary">
            <Typography component="span" fontWeight={600}>{uploadedCount}</Typography>/{MAX_DOCUMENTS} documents
          </Typography>
          <Button
            variant="contained"
            color="primary"
            onClick={startNewConversation}
            startIcon={<AddIcon />}
            sx={{ px: 2, py: 1, textTransform: 'none' }}
          >
            New Chat
          </Button>
        </Box>
      </Toolbar>
    </Container>
  </AppBar>
));

export default Header;
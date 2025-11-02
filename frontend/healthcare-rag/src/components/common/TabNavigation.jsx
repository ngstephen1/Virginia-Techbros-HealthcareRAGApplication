import React from 'react';
import { Box, Tabs, Tab } from '@mui/material';
import ChatBubbleOutlineIcon from '@mui/icons-material/ChatBubbleOutline';
import FilePresentIcon from '@mui/icons-material/FilePresent';
import HistoryIcon from '@mui/icons-material/History';

const TabNavigation = React.memo(({ activeTab, setActiveTab, uploadedCount, conversationCount }) => {
  const tabs = [
    { id: "chat", label: "Chat", icon: <ChatBubbleOutlineIcon />, count: null },
    { id: "documents", label: `Documents (${uploadedCount})`, icon: <FilePresentIcon />, count: uploadedCount },
    { id: "conversations", label: `History (${conversationCount})`, icon: <HistoryIcon />, count: conversationCount },
  ];

  const handleChange = (event, newValue) => {
    setActiveTab(newValue);
  };

  return (
    <Box sx={{ borderBottom: 1, borderColor: 'divider' }}>
      <Tabs 
        value={activeTab} 
        onChange={handleChange} 
        centered
        variant="fullWidth"
      >
        {tabs.map(tab => (
          <Tab 
            key={tab.id} 
            value={tab.id} 
            label={tab.label} 
            icon={tab.icon} 
            iconPosition="start"
            sx={{ textTransform: 'none', fontWeight: 600 }}
          />
        ))}
      </Tabs>
    </Box>
  );
});

export default TabNavigation;
const bodyParser = require('body-parser');
const express = require('express');
const mongoose = require('mongoose');
require('dotenv').config();
const cors = require('cors');
app.use(cors({ origin: 'https://ethics-checker-frontend.onrender.com' }));

const app = express();

// Test Route
app.get('/', (req, res) => {
    res.send('Server is running and connected to MongoDB');
});

app.use(bodyParser.json());

//Mock endpoint for user input
app.post('/api/analyze', (req, res) => {
    const { prompt } = req.body;
    if (!prompt) {
        return res.status(400).json({error: 'Prompt is required' });
    }
    res.json({ message: 'Prompt received', prompt});
});

// MongoDB Connection
mongoose
    .connect(process.env.MONGO_URI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB Connected'))
    .catch((err) => console.error(err));

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));

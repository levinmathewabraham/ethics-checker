const mongoose = require('mongoose');

const responseSchema = new mongoose.Schema({
    prompt: String,
    response: String,
    biasAnalysis: Object,
    ethicalScore: Number,
    timestamp: { type: Date, default: Date.now },
});

module.exports = mongoose.model('Response', responseSchema);

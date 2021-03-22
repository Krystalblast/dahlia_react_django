const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
 // entry: './src/index.js',
 mode: 'development',
 entry: {
    index: './src/index.js',
 },
 devtool: 'inline-source-map',
 devServer: {
   contentBase: path.resolve(__dirname, 'dist'),
   compress: true,
   port: 8081,
   historyApiFallback: true,
 },
 plugins: [
    new HtmlWebpackPlugin({
       template: 'src/index.html',
       inject: true,
       filename: 'index.html'
    }),
 ],
 output: {
    filename: '[name].bundle.js',
    path: path.resolve(__dirname, 'dist'),
    clean: true,
  },

  module: {
    rules: [
       //First Rule
        {
         test: /\.(js)$/,
         exclude: /node_modules/,
         use: ['babel-loader']
         },
      //Second Rule
        {
        test: /\.css$/i,
        use: ['style-loader', 'css-loader'],
        }
    ],
  },
  resolve: {
   extensions: ['*', '.js', '.jsx'],
 },
 externals:{
   config: JSON.stringify({
      apiUrl: 'http://localhost:8000'
   })
 },
};
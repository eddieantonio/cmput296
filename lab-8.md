% CMPUT 404 Lab 8
% Alexander Wong, Eddie Antonio Santos
% October 26, 2016

# Overview

 - Learn how to utilize WebSockets and Phaser.
 - Create a basic phaser game with WebSocket connectivity for real-time server to client communication.

[Phaser]: http://phaser.io/

# Steps

 #. Clone [this repository](https://github.com/CMPUT404W2016/CMPUT404LAB8_W2016/tree/ec4f12ff40d8f6500938e994a9c69e2084dcbff6).
 #. In the root, run `npm install`
 #. Run the application `./bin/www`
 #. Go to <http://phaser.io> and view some examples
 #. Navigate to <http://phaser.io/examples/v2/tilemaps/csv-map-collide>
 #. Create a new folder instead `public` called `assets`.
 #. Download the three necessary asset files and place them instead `public/assets`:
    - <https://github.com/photonstorm/phaser-examples/raw/master/examples/assets/tilemaps/csv/catastrophi_level2.csv>
    - <https://github.com/photonstorm/phaser-examples/blob/master/examples/assets/tilemaps/tiles/catastrophi_tiles_16.png>
    - <https://github.com/photonstorm/phaser-examples/blob/master/examples/assets/sprites/spaceman.png>
 #. Copy the code from this example and place it into `public/javascript/game.js`:
    - <https://github.com/photonstorm/phaser-examples/blob/master/examples/tilemaps/csv%20map%20collide.js>
 #. Rename `new Phaser.Game`'s 4th argument from `phaser-example` to `phaser`
    - To match the `<div>` ID we specified in the template.
 #. Modify the paths in  `preload()` to match the path we downloaded everything
    to---namely, `assets/` (the web framework removes the `public` part).
 #. (optional) Uncomment `layer.debug` to be `true` to see collision.
 #. Run the application again using `./bin/www`
 #. Stop the application. Add the WebSocket Client code to
    `public/javascripts/game.js`: <https://gist.github.com/awwong1/20b3acea02019f43a88f>
 #. Add the client WebSocket instantiation at the bottom of the `create()` method:

    ```javascript
    this.client = new Client();
    this.client.openConnection();
    ```
 #. Add in a UUID generator in the client. Create a new function with
    the following: <http://stackoverflow.com/a/105074/6626414>
 #. Update the server side code to handle players instead of the one
    rabbit object: <https://gist.github.com/awwong1/90d50ffa41cfc5ef7ea4>
 #. Set the variables of the class within `game.js` to equal the
    following:

    ```javascript
    var map;
    var layer;
    var cursors;
    var players = {};
    var id = guid();
    players[id] = {};
    var player = players[id];
    ```

 #. Add the following code to the bottom of the `update()` method:

    ```javascript
    if (this.client.connected) {
        this.client.ws.send(JSON.stringify({
            uuid: id,
            x: player.x,
            y: player.y
        });
    }
    ```

 #. Modify the client `onMessage()` function to equal the following:
    <https://gist.github.com/awwong1/2280e439b81c0fa666f7>
 #. Run the application. Open up a new browser window and run the
    application. What happens?
 #. (Bonus) Get the application working with up/down/left/right
    animations
 #. (Bonus) Get the WebSockets working with
    <http://phaser.io/examples/v2/tilemaps/csv-map-with-p2>

# Questions

 #. What is a WebSocket? Why were they created?
 #. What is long-polling? Briefly explain what code you would need in
    the browser-side JavaScript and what code you would need the
    server-side to enable long-polling.
 #. What does the constructor of the `Client` class do?
 #. Why should WebSockets be used instead of long-polling?
 #. What is Phaser (in the context of this lab)?

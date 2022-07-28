import {createClient} from 'redis';
import { promisify } from 'util';

class RedisClient {
  constructor() {
    this.client = createClient();
    this.client.on('error', (err) => console.log(err.message));
  }

  isAlive() {
    return this.client.connected;
  }

  async get(key) {
    const value = promisify(this.client.get).bind(this.client);
    return value(key);
  }

  async set(key, value, duration) {
    await this.client.set(key, value, "EX", duration);
  }

  async del(key) {
    await this.client.del(key);
  }
}

const redisClient = new RedisClient();
module.exports = redisClient;
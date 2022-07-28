import { MongoClient, Server } from 'mongodb';

class DBClient {
  constructor() {
    this.host = process.env.DB_HOST || 'localhost';
    this.port = process.env.DB_PORT || 27017;
    this.database = process.env.DB_DATABASE || 'files_manager';

    this.client = new MongoClient(new Server(this.host, this.port), { native_parser: true });
    this.client.connect();
    this.db = this.client.db(this.database);
  }

  isAlive() {
    return !!this.client.topology && this.client.topology.isConnected();
  }

  async nbUsers() {
    const countUsers = await this.db.collection('users').estimatedDocumentCount();
    return countUsers;
  }

  async nbFiles() {
    const countFiles = await this.db.collection('files').estimatedDocumentCount();
    return countFiles;
  }
}

const dbClient = new DBClient();
module.exports = dbClient;
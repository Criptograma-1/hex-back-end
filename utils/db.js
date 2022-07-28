import { MongoClient } from ('mongodb')

class DBClient {
  constructor() {
    this.host = process.env.DB_HOST || 'localhost';
    this.port = process.env.DB_PORT || 27017;
    this.database = process.env.DB_DATABASE || 'files_manager';

    this.client = new MongoClient(`mongodb://${this.host}:${this.port}`);
    await this.client.connect();
    this.db = this.client.db(this.database);
  }

  isAlive() {
    return this.client.topology.isConnected();
  }

  async nbUsers() {
    let countUsers = await this.db.collection('users').estimatedDocumentCount();
    return countUsers;
  }

  async nbFiles() {
    let countFiles = await this.db.collection('files').estimatedDocumentCount();
    return countFiles;
  }

}

const dbClient = new DBClient();
module.exports = dbClient;
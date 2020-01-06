import { Sequelize, Model, DataTypes, BuildOptions} from 'sequelize'
//import * as path from 'path'
//let env = process.env.NODE_ENV || 'development';

export default class People extends Model{
    public id !: number;
    public name !: string;
    public hobby !: string;
}


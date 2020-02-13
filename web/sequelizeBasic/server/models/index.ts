import { Sequelize, DataTypes} from 'sequelize'
import People from './friend'
import config from '../config/config'

export function init(): Sequelize{
    const sequelize: Sequelize = new Sequelize(config.mysql.key);
    People.init({
        id:{
            type: DataTypes.INTEGER.UNSIGNED,
            autoIncrement: true,
            primaryKey: true,
        },
        name:{
            type: new DataTypes.STRING(128),
            allowNull:false,
        },
        hobby:{
            type: new DataTypes.STRING(128),
            allowNull:true,
        }
    },{
            sequelize,
            tableName: 'people',
            timestamps: false,
            freezeTableName: true,
    });

    return sequelize;
}
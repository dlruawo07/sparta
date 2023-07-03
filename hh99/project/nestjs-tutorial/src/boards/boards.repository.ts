import { DataSource, DeleteResult, Repository } from 'typeorm';
import { Board } from './board.entity';
import { InjectRepository } from '@nestjs/typeorm';
import { CreateBoardDto } from './dto/create-board.dto';
import { BoardStatus } from './board-status.enum';
import { User } from 'src/auth/user.entity';
import { NotFoundException } from '@nestjs/common';

export class BoardRepository extends Repository<Board> {
  constructor(@InjectRepository(Board) private dataSource: DataSource) {
    super(Board, dataSource.manager);
  }

  async getAllBoards(): Promise<Board[]> {
    return await this.find();
  }

  async getMyBoards(user: User): Promise<Board[]> {
    const query = this.createQueryBuilder('board');
    query.where('board.userId = :userId', { userId: user.id });
    const boards = await query.getMany();

    return boards;
  }

  async createBoard(
    createBoardDto: CreateBoardDto,
    user: User,
  ): Promise<Board> {
    const { title, description } = createBoardDto;

    const board = this.create({
      title,
      description,
      status: BoardStatus.PUBLIC,
      user,
    });

    await this.save(board);
    return board;
  }

  async getBoardById(id: number): Promise<Board> {
    return await this.findOne({ where: { id } });
  }

  async deleteBoard(id: number, user: User): Promise<DeleteResult> {
    return await this.delete({ id, user: { id: user.id } });
  }

  async updateBoardStatus(
    id: number,
    status: BoardStatus,
    user: User,
  ): Promise<Board> {
    const board = await this.findOne({ where: { id, user: { id: user.id } } });

    if (!board) {
      throw new NotFoundException(`Can't find board with id ${id}`);
    }

    board.status = status;
    await this.save(board);

    return board;
  }
}

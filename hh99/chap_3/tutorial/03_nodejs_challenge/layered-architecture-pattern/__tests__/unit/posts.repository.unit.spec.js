const PostsRepository = require("../../repositories/posts.repository.js");

// posts.repository.js 에서는 아래 5개의 Method만을 사용합니다.
let mockPostsModel = {
  findAll: jest.fn(),
  create: jest.fn(),
};

let postsRepository = new PostsRepository(mockPostsModel);

describe("Layered Architecture Pattern Posts Repository Unit Test", () => {
  // 각 test가 실행되기 전에 실행됩니다.
  beforeEach(() => {
    jest.resetAllMocks(); // 모든 Mock을 초기화합니다.
  });

  test("Posts Repository findAllPost Method", async () => {
    mockPostsModel.findAll = jest.fn(() => {
      return "findAll Result";
    });

    const posts = await postsRepository.findAllPost();

    expect(mockPostsModel.findAll).toHaveBeenCalledTimes(1);

    expect(posts).toEqual("findAll Result");
  });

  test("Posts Repository createPost Method", async () => {
    mockPostsModel.create = jest.fn(() => {
      return "Create Result";
    });

    const createPostParams = {
      nickname: "abc",
      password: "pwd",
      title: "title",
      content: "content",
    };

    const post = await postsRepository.createPost(
      createPostParams.nickname,
      createPostParams.password,
      createPostParams.title,
      createPostParams.content
    );
    expect(mockPostsModel.create).toHaveBeenCalledTimes(1);

    expect(post).toEqual("Create Result");

    expect(mockPostsModel.create).toHaveBeenCalledWith({
      nickname: createPostParams.nickname,
      password: createPostParams.password,
      title: createPostParams.title,
      content: createPostParams.content,
    });
  });
});

from panda3d.core import Texture, TexturePool, LoaderOptions, TextureStage, TexGenAttrib, TransformState

class SkyBox:
    def __init__(self):
        lo = LoaderOptions(flags = LoaderOptions.TF_generate_mipmaps)
        
        texture_cube_map = Texture("world_cube_map")
        texture_cube_map.setup_cube_map()
        texture_cube_map.read(fullpath = 'assets/textures/skybox1/right.png',  z = 0, n = 0, read_pages = False, read_mipmaps = False, options = lo)
        texture_cube_map.read(fullpath = 'assets/textures/skybox1/left.png',   z = 1, n = 0, read_pages = False, read_mipmaps = False, options = lo)
        texture_cube_map.read(fullpath = 'assets/textures/skybox1/bottom.png', z = 2, n = 0, read_pages = False, read_mipmaps = False, options = lo)
        texture_cube_map.read(fullpath = 'assets/textures/skybox1/top.png',    z = 3, n = 0, read_pages = False, read_mipmaps = False, options = lo)
        texture_cube_map.read(fullpath = 'assets/textures/skybox1/front.png',  z = 4, n = 0, read_pages = False, read_mipmaps = False, options = lo)
        texture_cube_map.read(fullpath = 'assets/textures/skybox1/back.png',   z = 5, n = 0, read_pages = False, read_mipmaps = False, options = lo)
        
        TexturePool.add_texture(texture_cube_map)
        
        skybox = loader.load_model('assets/models/sphere.bam')
        skybox.reparent_to(render)
        skybox.set_texture(texture_cube_map)
        
        ts = TextureStage.get_default()
        
        skybox.set_tex_gen(ts, TexGenAttrib.M_world_cube_map)
        skybox.set_tex_hpr(ts, (0, 90, 180))
        skybox.set_tex_scale(ts, (1, -1))
        skybox.set_light_off()
        skybox.set_material_off()
        skybox.setScale(1000)
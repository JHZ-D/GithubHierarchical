import os

JAVADOC_GLOBAL_NAME = 'javadoc'
#分析用的APIdoc的路径
APIDOC_PATH = 'C:/workspace/SOworkspace/apidocs/'
#最后把最后成品concept map会放在这里，目前啥也没有
CONCEPT_MAP_STORE_PATH = 'C:/workspace/SOworkspace/data/concept_map/'

JAVADOC_CONCEPT_MAP_FILE_NAME = 'concept_map_javadoc.gexf'
JAVADOC_PATH = os.path.join(APIDOC_PATH, 'javadocs')
TEMP_FILE_STORE_PATH = 'C:/workspace/SOworkspace/data/cache/'
#生成concept map后图数据存储的路径，在开发中会变化
LATEST_CONCEPT_MAP_PATH = {
    JAVADOC_GLOBAL_NAME : 'C:/workspace/SOworkspace/backup/concept_map_javadoc20200801.gexf'
}

#为实现HERMES mk1需要分析文档语义，因此将所有概念描述抽出并存放与此
APIDOC_DESCRIPTION_STORE_PATH = {
    JAVADOC_GLOBAL_NAME : 'C:/workspace/SOworkspace/data/apidoc_description/javadoc_descriptions.pkl'
}

#为实现HERMES mk1需要尝试在文档描述中抽取wiki中的常见concept，因此将wikipedia的内容存储路径纪录在此
WIKIPEDIA_CONCEPT_STORE_PATH = {
    'text': 'C:/workspace/SOworkspace/data/wikipedia_concepts/text_content/'
}

#MYSQL属性
Mysql_addr = "162.105.16.32"
Mysql_user = "root"
Mysql_password = "root"
Mysql_dbname_sotorrent = "sotorrent20_03"